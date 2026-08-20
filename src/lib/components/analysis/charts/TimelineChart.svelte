<script>
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";
  import { onMount, onDestroy } from "svelte";
  import * as d3 from "d3";
  import shows from "../../../../../public/data/shows.json";

  let svgElement;
  let circles;

  // 🟢 Reactive scale only
  const colorScale = $derived(
    d3
      .scaleOrdinal()
      .domain([...new Set(shows.map((d) => d.Borough))])
      .range(["#16FF00", "#008BFF", "#5B23FF", "#000000", "#FF0B55"]),
  );

  const parser = d3.timeParse("%Y-%m-%d %H:%M:%S");
  const data = shows.map((d) => ({ ...d, date: parser(d.Date) }));

  const width = 640;
  const height = 300;
  const radius = 6.5;
  const margin = 40;

  const xScale = d3
    .scaleTime()
    .domain(d3.extent(data, (d) => d.date))
    .range([margin, width - margin]);

  const byDate = d3.group(data, (d) => d.date.getTime());
  byDate.forEach((items) => {
    const targetX = xScale(items[0].date);
    items.forEach((item) => {
      item.x = targetX;
      item.targetX = targetX;
      item.y = height / 2;
    });
  });

  let simulation;
  let tooltipDiv; // 🔴 Add this ref instead of creating DOM inside onMount

  onMount(() => {
    // Create tooltip div once at mount
    tooltipDiv = document.createElement("div");
    Object.assign(tooltipDiv.style, {
      position: "absolute",
      background: "rgba(255, 255, 255, 0.975)",
      border: "3px solid #ff00d4",
      padding: "4px 8px",
      borderRadius: "4px",
      fontSize: "14px",
      pointerEvents: "none",
      display: "none",
      zIndex: "100",
    });
    document.body.appendChild(tooltipDiv);

    simulation = d3
      .forceSimulation(data)
      .force("x", d3.forceX((d) => d.targetX).strength(1.5))
      .force("y", d3.forceY(height / 2).strength(0.15))
      .force("collide", d3.forceCollide(radius))
      .alpha(1)
      .restart();

    for (let i = 0; i < 500; i++) simulation.tick();
    simulation.stop();

    d3.select(svgElement)
      .append("g")
      .attr("transform", `translate(0,${height - margin})`)
      .call(d3.axisBottom(xScale).ticks(6));

    circles = d3
      .select(svgElement)
      .append("g")
      .selectAll("circle")
      .data(data)
      .join("circle")
      .attr("r", radius)
      .attr("cx", (d) => d.x)
      .attr("cy", (d) => d.y)
      .attr("fill", (d) => colorScale(d.Borough))
      .attr("stroke", "#fff")
      .on("mouseover", (e, d) => {
        tooltipDiv.innerHTML = `<strong>${d.Artist}</strong><br/>${d.Venue}<br/>${d.date.toLocaleDateString("en-gb")}<br/>${d.Borough}`;
        Object.assign(tooltipDiv.style, {
          display: "block",
          left: e.pageX + 10 + "px",
          top: e.pageY - 10 + "px",
        });
      })
      .on("mouseout", () => {
        tooltipDiv.style.display = "none";
      });

    return () => {
      simulation.stop();
      tooltipDiv.remove(); // Clean up
    };
  });

  $effect(() => {
    if (data.length && circles) {
      circles.data(data);
      simulation.nodes(data);
      simulation.alpha(1).restart();
    }
  });
</script>

<BaseChartPanel title="Timeline">
  <svg bind:this={svgElement} {width} {height}></svg>
</BaseChartPanel>
