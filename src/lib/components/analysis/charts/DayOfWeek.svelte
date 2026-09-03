<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import { onMount } from "svelte";
  import shows from "../../../../../public/data/shows.json";
  import * as d3 from "d3";

  let daysArray = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];

  // count shows per day, then map to daysArray order (fixes the ordering bug)
  let dayCountsRaw = {};
  for (let show of shows) {
    dayCountsRaw[show.Day] = (dayCountsRaw[show.Day] ?? 0) + 1;
  }
  let data = daysArray.map((day) => ({
    day,
    count: dayCountsRaw[day] ?? 0,
  }));

  // margin convention
  const margin = { top: 10, right: 20, bottom: 30, left: 80 };
  const innerWidth = 250;
  const innerHeight = 150;
  const width = innerWidth + margin.left + margin.right;
  const height = innerHeight + margin.top + margin.bottom;

  let xScale = d3.scaleLinear().domain([0, 50]).range([0, innerWidth]);
  let yScale = d3
    .scaleBand()
    .domain(daysArray)
    .range([0, innerHeight])
    .padding(1);

  let svgEl;
  let tooltip = {};

  onMount(() => {
    const svg = d3.select(svgEl).attr("width", width).attr("height", height);

    const g = svg
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.selectAll("rect")
      .data(data)
      .join("rect")
      .attr("x", 0)
      .attr("y", (d) => yScale(d.day))
      .attr("width", (d) => xScale(d.count))
      .attr("height", 15)
      .attr("fill", "#ff00d440")
      .attr("stroke", "black")
      .on("mouseenter", (event, d) =>
        tooltip.show(
          event,
          `Since 2022 I've attended </br><strong>${d.count} shows on ${d.day + "s"}</strong>`,
          "#ff00d4",
        ),
      )
      .on("mouseleave", () => tooltip.hide());
    g.append("g").call(d3.axisLeft(yScale)).style("stroke-width", 2);

    g.append("g")
      .attr("transform", `translate(0,${innerHeight})`)
      .call(d3.axisBottom(xScale))
      .style("stroke-width", 2);
  });
</script>

<ChartWrapper title="Days of the Week">
  {#snippet children(show, hide)}
    {@const _ = ((tooltip.show = show), (tooltip.hide = hide))}
    <svg bind:this={svgEl}></svg>
  {/snippet}
</ChartWrapper>
