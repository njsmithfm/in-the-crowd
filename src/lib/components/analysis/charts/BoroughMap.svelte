<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import ChartWrapper from "../ChartWrapper.svelte";
  import shows from "../../../../../public/data/shows.json";
  import boroughs from "./boroughs.json";
  import venueLocations from "./venueLocations.json";
  import { boroughColors } from "../boroughColors.js";

  const locationsByVenue = new Map(
    venueLocations.features.map((feature) => [
      feature.properties.label.trim(),
      feature.geometry.coordinates,
    ]),
  );

  let svgEl;
  let tooltip = {};

  onMount(() => {
    const width = 400;
    const height = 400;

    const venueData = Array.from(
      d3.rollup(
        shows,
        (venueShows) => ({
          count: venueShows.length,
          borough: venueShows[0].Borough.trim(),
          shows: venueShows,
        }),
        (show) => show.Venue.trim(),
      ),
      ([label, data]) => ({
        label,
        ...data,
        coordinates: locationsByVenue.get(label),
      }),
    ).filter((venue) => venue.coordinates);

    const projection = d3.geoMercator().fitSize([width, height], boroughs);

    const path = d3.geoPath(projection);

    const radius = d3
      .scaleSqrt()
      .domain([0, d3.max(venueData, (venue) => venue.count) ?? 1])
      .range([2, 10]);

    const marker = d3.select(svgEl).attr("viewBox", `0 0 ${width} ${height}`);

    marker.selectAll("*").remove();

    const mapLayer = marker.append("g").attr("class", "map-layer");

    mapLayer
      .selectAll(".borough")
      .data(boroughs.features)
      .join("path")
      .attr("class", "borough")
      .attr("d", path)
      .attr("fill", "#eee")
      .attr("stroke", "#222")
      .attr("stroke-width", 1);

    const venueLayer = mapLayer.append("g").attr("class", "venue-layer");
    const venueStrokeWidth = 1;
    venueLayer
      .selectAll(".venue")
      .data(venueData)
      .join("circle")
      .attr("class", "venue")
      .attr("cx", (venue) => projection(venue.coordinates)[0])
      .attr("cy", (venue) => projection(venue.coordinates)[1])
      .attr("r", (venue) => radius(venue.count))
      .attr("fill", (venue) => boroughColors[venue.borough] || "#111")
      .attr("fill-opacity", 0.5)
      .attr("stroke", "#111")
      .attr("stroke-width", venueStrokeWidth)
      .on("mouseenter", (event, venue) => {
        tooltip.show(
          event,
          `<strong>${venue.label}</strong><br/>
             ${venue.count} ${venue.count === 1 ? "show" : "shows"}<br/>
             ${venue.borough}`,
          boroughColors[venue.borough] || "#111",
        );
      })
      .on("mouseleave", () => tooltip.hide());
    const zoom = d3
      .zoom()
      .scaleExtent([1, 8])
      .translateExtent([
        [0, 0],
        [width, height],
      ])
      .on("zoom", (event) => {
        mapLayer.attr("transform", event.transform);
        venueLayer
          .selectAll(".venue")
          .attr("r", (venue) => radius(venue.count) / event.transform.k)
          .attr("stroke-width", venueStrokeWidth / event.transform.k);
      });

    marker.call(zoom);
  });
</script>

<ChartWrapper title="Map" subtitle="(Zoom for detail)">
  {#snippet children(show, hide)}
    {@const _ = ((tooltip.show = show), (tooltip.hide = hide))}
    <svg bind:this={svgEl}></svg>
  {/snippet}
</ChartWrapper>
