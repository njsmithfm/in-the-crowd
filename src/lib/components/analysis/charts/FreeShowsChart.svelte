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

  let freeShows = shows.filter((s) => s.Free_Show);
  let years = [...new Set(freeShows.map((s) => s.Year))].sort(d3.ascending);
  let counts = years.map((y) => ({
    year: String(y),
    count: freeShows.filter((s) => s.Year === y).length,
  }));

  let xScale = d3
    .scaleBand()
    .domain(counts.map((d) => d.year))
    .range([0, innerWidth])
    .padding(0.3);
  let yScale = d3
    .scaleLinear()
    .domain([0, d3.max(counts, (d) => d.count)])
    .nice()
    .range([innerHeight, 0]);

  let svgEl;
  let tooltip = {};

  onMount(() => {
    const g = d3
      .select(svgEl)
      .attr("viewBox", `0 0 ${width} ${height}`)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.selectAll("rect")
      .data(counts)
      .join("rect")
      .attr("x", (d) => xScale(d.year))
      .attr("y", (d) => yScale(d.count))
      .attr("width", xScale.bandwidth())
      .attr("height", (d) => innerHeight - yScale(d.count))
      .attr("fill", "#ff00d440")
      .attr("stroke", "black")
      .on("mouseenter", (e, d) =>
        tooltip.show(
          e,
          `<strong>${d.count}</strong> free show${d.count > 1 ? "s" : ""}<br>attended in <strong>${d.year}</strong>`,
          "#ff00d4",
        ),
      )
      .on("mouseleave", () => tooltip.hide());

    g.append("g")
      .call(d3.axisLeft(yScale))
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

<ChartWrapper title="Free Shows by Year">
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
