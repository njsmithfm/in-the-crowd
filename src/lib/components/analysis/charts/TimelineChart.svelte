<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import * as d3 from "d3";
  import { boroughColors } from "../boroughColors.js";
  import shows from "../../../../../public/data/shows.json";

  const width = 640;
  const height = 300;
  const radius = 6.5;
  const margin = 40;

  const parser = d3.timeParse("%Y-%m-%d %H:%M:%S");
  const data = shows.map((show) => ({ ...show, date: new Date(show.Date) }));

  const xScale = d3
    .scaleTime()
    .domain(d3.extent(data, (show) => show.date))
    .range([margin, width - margin]);

  // x-axis
  const ticks = [
    xScale.domain()[0],
    ...d3.timeYears(xScale.domain()[0], xScale.domain()[1]),
  ];
  // Pre-compute positions once (run simulation, then freeze)
  let processedData = $state([]);

  function computePositions() {
    data.forEach((show) => {
      show.targetX = xScale(show.date);
      show.x = show.targetX;
      show.y = height / 2;
    });

    const simulation = d3
      .forceSimulation(data)
      .force("x", d3.forceX((d) => d.targetX).strength(1.5))
      .force("y", d3.forceY(height / 2).strength(0.15))
      .force("collide", d3.forceCollide(radius + 0.5))
      .alpha(1)
      .restart();

    // Run for fixed iterations until stable
    for (let i = 0; i < 100; i++) simulation.tick();
    simulation.stop();

    processedData = data;
  }

  // Compute on init
  computePositions();

  // Svelte state for tooltip
  let tooltipState = $state({
    visible: false,
    x: 0,
    y: 0,
    content: "",
    borderColor: "#333",
  });

  function showTooltip(e, content, borderColor = "#333") {
    tooltipState = {
      visible: true,
      x: e.clientX,
      y: e.clientY,
      content,
      borderColor,
    };
  }
  function hideTooltip() {
    tooltipState.visible = false;
  }
</script>

<ChartWrapper title="Timeline">
  {#snippet children(showTooltip, hideTooltip)}
    <svg viewBox={`0 0 ${width} ${height}`}>
      <line
        x1={margin}
        x2={width - margin}
        y1={height - margin}
        y2={height - margin}
        stroke="#333"
        stroke-width={2}
      />

      {#each ticks as year}
        <g transform={`translate(${xScale(year)}, ${height - margin})`}>
          <!-- tick mark -->
          <line y2={5} stroke="#333" stroke-width={2} />
          <!-- label -->
          <text y={18} text-anchor="middle" font-size={16} fill="#333">
            {d3.timeFormat("%Y")(year)}
          </text>
        </g>
      {/each}

      {#each processedData as item}
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <circle
          cx={item.x}
          cy={item.y}
          r={radius}
          fill={boroughColors[item.Borough] || "#000"}
          stroke="#fff"
          onmouseenter={(e) =>
            showTooltip(
              e,
              `<strong>${item.Artist}</strong><br/>${item.Venue}<br/>${item.date.toLocaleDateString("en-gb", { year: "numeric", month: "long", day: "numeric" })}<br/>${item.Borough}`,
              boroughColors[item.Borough],
            )}
          onmouseleave={hideTooltip}
        />
      {/each}
    </svg>
  {/snippet}
</ChartWrapper>
