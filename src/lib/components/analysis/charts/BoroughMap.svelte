<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import ChartWrapper from "../ChartWrapper.svelte";
  import shows from "../../../../../public/data/shows.json";
  import boroughs from "./boroughs.json";

  let svgEl;
  let tooltip = {};

  onMount(() => {
    const width = 640;
    const height = 400;

    const countByBorough = d3.rollup(
      shows,
      (items) => items.length,
      (show) => show.Borough.trim(),
    );

    const maxCount = d3.max([...countByBorough.values()]) ?? 1;

    const color = d3
      .scaleSequential(d3.interpolateYlOrRd)
      .domain([0, maxCount]);

    const projection = d3.geoMercator().fitSize([width, height], boroughs);

    const path = d3.geoPath(projection);

    const boroughMap = d3.select(svgEl);

    boroughMap
      .attr("viewBox", `0 0 ${width} ${height}`)
      .selectAll("path")
      .data(boroughs.features)
      .join("path")
      .attr("d", path)
      .attr("fill", (feature) => {
        const borough = feature.properties.BoroName;
        return color(countByBorough.get(borough) ?? 0);
      })
      .attr("stroke", "#111")
      .attr("stroke-width", 1)
      .on("mouseenter", (event, feature) => {
        const borough = feature.properties.BoroName;
        const count = countByBorough.get(borough) ?? 0;

        tooltip.show(
          event,
          `<strong>${borough}</strong><br/>${count} ${
            count === 1 ? "show" : "shows"
          }`,
          color(count),
        );
      })
      .on("mouseleave", () => tooltip.hide());
  });
</script>

<ChartWrapper title="Shows by Borough">
  {#snippet children(show, hide)}
    {@const _ = ((tooltip.show = show), (tooltip.hide = hide))}
    <svg bind:this={svgEl}></svg>
  {/snippet}
</ChartWrapper>
