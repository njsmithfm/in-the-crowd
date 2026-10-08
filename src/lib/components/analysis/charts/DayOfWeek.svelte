<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import { onMount } from "svelte";
  import shows from "../../../../../public/data/shows.json";
  import * as d3 from "d3";

  const margin = { top: 20, right: 20, bottom: 40, left: 60 };
  const innerWidth = 500;
  const innerHeight = 280;
  const width = innerWidth + margin.left + margin.right;
  const height = innerHeight + margin.top + margin.bottom;

  const daysArray = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];
  let dayCounts = {};
  for (let show of shows) {
    dayCounts[show.Day] = (dayCounts[show.Day] ?? 0) + 1;
  }
  let data = daysArray.map((day) => ({ day, count: dayCounts[day] ?? 0 }));

  let xScale = d3.scaleLinear().domain([0, 50]).range([0, innerWidth]);
  let yScale = d3
    .scaleBand()
    .domain(daysArray)
    .range([0, innerHeight])
    .padding(0.25);

  let svgEl;
  let tooltip = {};

  onMount(() => {
    const g = d3
      .select(svgEl)
      .attr("viewBox", `0 0 ${width} ${height}`)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.selectAll("rect")
      .data(data)
      .join("rect")
      .attr("x", 0)
      .attr("y", (d) => yScale(d.day))
      .attr("width", (d) => xScale(d.count))
      .attr("height", 25)
      .attr("fill", "#ff00d440")
      .attr("stroke", "black")
      .on("mouseenter", (e, d) =>
        tooltip.show(
          e,
          `<strong>${d.count}</strong> shows attended<br>on <strong>${d.day}s</strong>`,
          "#ff00d4",
        ),
      )
      .on("mouseleave", () => tooltip.hide());

    const yAxis = g.append("g").call(d3.axisLeft(yScale));
    yAxis.selectAll("text").text(
      (d) =>
        ({
          Monday: "Mon",
          Tuesday: "Tues",
          Wednesday: "Wed",
          Thursday: "Thurs",
          Friday: "Fri",
          Saturday: "Sat",
          Sunday: "Sun",
        })[d],
    );
    yAxis
      .selectAll("*")
      .attr("stroke", "#333")
      .attr("stroke-width", 1)
      .style("font-size", "16px");
    g.append("g")
      .attr("transform", `translate(0,${innerHeight})`)
      .call(d3.axisBottom(xScale))
      .selectAll("*")
      .attr("stroke", "#333")
      .attr("stroke-width", 1)
      .style("font-size", "16px");
  });
</script>

<ChartWrapper title="Days of the Week">
  {#snippet children(show, hide)}
    {@const _ = ((tooltip.show = show), (tooltip.hide = hide))}
    <svg bind:this={svgEl}></svg>
  {/snippet}
</ChartWrapper>

<style>
  svg {
    display: block;
    width: 100%;
    height: auto;
  }
</style>
