<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import shows from "../../../../../public/data/shows.json";
  import ChartWrapper from "../ChartWrapper.svelte";
  let svgEl;
  let tooltip = {};
  onMount(() => {
    const width = 640;
    const height = 320;
    const margin = { top: 20, right: 20, bottom: 40, left: 40 };

    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const counts = Array.from(
      d3.rollup(
        shows.filter((show) => show.Free_Show),
        (items) => items.length,
        (show) => show.Year,
      ),
      ([year, count]) => ({ year: String(year), count }),
    ).sort((a, b) => d3.ascending(a.year, b.count));

    const x = d3
      .scaleBand()
      .domain(counts.map((d) => d.year))
      .range([0, innerWidth])
      .padding(0.2);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(counts, (d) => d.count) ?? 0])
      .nice()
      .range([innerHeight, 0]);

    const root = d3.select(svgEl);
    root.selectAll("*").remove();

    const g = root
      .attr("viewBox", `0 0 ${width} ${height}`)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.append("g").call(d3.axisLeft(y).ticks(4)).style("stroke-width", 2);

    g.selectAll("rect")
      .data(counts)
      .join("rect")
      .attr("x", (d) => x(d.year))
      .attr("y", (d) => y(d.count))
      .attr("width", x.bandwidth())
      .attr("height", (d) => innerHeight - y(d.count))
      .attr("fill", "#ff00d440")
      .attr("stroke", "black")
      .on("mouseenter", (event, d) =>
        tooltip.show(
          event,

          `<strong>${d.count} ${d.count === 1 ? "free show" : "free shows"}</strong></br>attended in ${d.year}`,
          "#ff00d4",
        ),
      )
      .on("mouseleave", () => tooltip.hide());

    g.append("g")
      .attr("transform", `translate(0,${innerHeight})`)
      .call(d3.axisBottom(x))
      .style("stroke-width", 2);
  });
</script>

<ChartWrapper title="Free Shows by Year">
  {#snippet children(show, hide)}
    {@const _ = ((tooltip.show = show), (tooltip.hide = hide))}
    <svg bind:this={svgEl}></svg>
  {/snippet}
</ChartWrapper>

<style>
</style>
