<script>
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import shows from "../../../../../public/data/shows.json";

  let svgElement;
  let tooltip;

  onMount(() => {
    const width = 640;
    const height = 300;
    const radius = 6.5;
    const margin = 40;

    const parser = d3.timeParse("%Y-%m-%d %H:%M:%S");
    const data = shows.map((d) => ({ ...d, date: parser(d.Date) }));

    const xScale = d3
      .scaleTime()
      .domain(d3.extent(data, (d) => d.date))
      .range([margin, width - margin]);

    const yValues = [...new Set(shows.map((d) => d.Borough))];
    const colorScale = d3
      .scaleOrdinal()
      .domain(yValues)
      .range(["#16FF00", "#008BFF", "#5B23FF", "#000000", "#FF0B55"]);

    // Group by date and assign fixed X positions
    const byDate = d3.group(data, (d) => d.date.getTime());

    byDate.forEach((items, timestamp) => {
      const targetX = xScale(items[0].date);
      items.forEach((item) => {
        item.x = targetX; // Fixed X for this date
        item.targetX = targetX; // Store target for strong force
        item.y = height / 2; // Start at center
      });
    });

    // Beeswarm simulation: strong X constraint + collision
    const simulation = d3
      .forceSimulation(data)
      .force("x", d3.forceX((d) => d.targetX).strength(1.5)) // Very strong X lock
      .force("y", d3.forceY(height / 2).strength(0.15)) // Minimal Y influence
      .force("collide", d3.forceCollide(radius)) // Tight collision
      .alpha(1)
      .restart();

    // Iterate to settle
    for (let i = 0; i < 500; i++) simulation.tick();
    simulation.stop();

    tooltip = d3
      .select("body")
      .append("div")
      .style("position", "absolute")
      .style("background", "rgba(255, 255, 255, 0.975)")
      .style("border", "3px solid #ff00d4")
      .style("color", "#000000")
      .style("padding", "4px 8px")
      .style("border-radius", "4px")
      .style("font-size", "14px")
      .style("pointer-events", "none");

    d3.select(svgElement)
      .append("g")
      .attr("transform", `translate(0,${height - margin})`)
      .call(d3.axisBottom(xScale).ticks(6));

    d3.select(svgElement)
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
        tooltip
          .style("opacity", 1)
          .html(
            `<strong>${d.Artist}</strong><br/>${d.Venue}<br/>${d.date.toLocaleDateString("en-gb", { day: "numeric", month: "long", year: "numeric" })}<br/>${d.Borough}`,
          )
          .style("left", e.pageX + 10 + "px")
          .style("top", e.pageY - 10 + "px");
      })
      .on("mouseout", () => tooltip.style("opacity", 0));
  });
</script>

<BaseChartPanel title="Timeline">
  <div class="chart-svg">
    <svg bind:this={svgElement} width="640" height="320"></svg>
  </div>
</BaseChartPanel>
