<script>
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import shows from "../../../../../public/data/shows.json";

  let svgElement;
  let tooltip;

  onMount(() => {
    const width = 640;
    const height = 200;
    const radius = 5;
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
      .range(["#ff7f0e", "#1f77b4", "#2ca02c"]);

    const simulation = d3
      .forceSimulation(data)
      .force("x", d3.forceX((d) => xScale(d.date)).strength(0.1))
      .force("y", d3.forceY(height / 2).strength(0.02))
      .force("collide", d3.forceCollide(radius + 0.5))
      .alpha(1)
      .restart();

    while (simulation.alpha() > 0.005) simulation.tick();
    simulation.stop();
    tooltip = d3
      .select("body")
      .append("div")
      .style("position", "absolute")
      .style("background", "#333")
      .style("color", "#fff")
      .style("padding", "4px 8px")
      .style("border-radius", "4px")
      .style("font-size", "12px")
      .style("pointer-events", "none")
      .style("opacity", 0);

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
            `<strong>${d.Artist}</strong><br/>${d.Venue}<br/>${d.date.toDateString()}<br/>${d.Borough}`,
          )
          .style("left", e.pageX + 10 + "px")
          .style("top", e.pageY - 10 + "px");
      })
      .on("mouseout", () => tooltip.style("opacity", 0));
  });
</script>

<BaseChartPanel title="Timeline" subtitle="(I rock through time)">
  <div class="chart-svg">
    <svg bind:this={svgElement} width="640" height="320"></svg>
  </div>
</BaseChartPanel>
