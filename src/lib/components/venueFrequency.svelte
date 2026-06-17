<script>
  import * as d3 from "d3";
  import { onMount } from "svelte";
  import shows from "../../../public/data/shows.json";

  let svgElement;

  onMount(() => {
    if (!svgElement) return;

    // Count shows by venue
    const venueCount = {};
    shows.forEach((show) => {
      venueCount[show.Venue] = (venueCount[show.Venue] || 0) + 1;
    });

    // Sort and take top 10
    const data = Object.entries(venueCount)
      .map(([venue, count]) => ({ venue, count }))
      .sort((a, b) => b.count - a.count)
      .slice(0, 10);

    const margin = { top: 20, right: 30, bottom: 60, left: 10 };
    const width = 400 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    // Clear existing
    d3.select(svgElement).selectAll("*").remove();

    const svg = d3
      .select(svgElement)
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    const xScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.count)])
      .range([0, width]);

    const yScale = d3
      .scaleBand()
      .domain(data.map((d) => d.venue))
      .range([0, height])
      .padding(0.1);

    // Bars
    svg
      .selectAll(".bar")
      .data(data)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("y", (d) => yScale(d.venue))
      .attr("height", yScale.bandwidth())
      .attr("x", 0)
      .attr("width", (d) => xScale(d.count))
      .attr("fill", "#4caf50");

    // Y-axis labels
    svg
      .selectAll(".label")
      .data(data)
      .enter()
      .append("text")
      .attr("class", "label")
      .attr("y", (d) => yScale(d.venue) + yScale.bandwidth() / 2)
      .attr("x", -5)
      .attr("text-anchor", "end")
      .attr("dominant-baseline", "middle")
      .attr("font-size", "12px")
      .text((d) => d.venue);

    // Count labels
    svg
      .selectAll(".count")
      .data(data)
      .enter()
      .append("text")
      .attr("class", "count")
      .attr("y", (d) => yScale(d.venue) + yScale.bandwidth() / 2)
      .attr("x", (d) => xScale(d.count) + 5)
      .attr("dominant-baseline", "middle")
      .attr("font-size", "12px")
      .attr("font-weight", "bold")
      .text((d) => d.count);

    // Title
    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", -5)
      .attr("text-anchor", "middle")
      .attr("font-size", "14px")
      .attr("font-weight", "bold")
      .text("Top 10 Venues");
  });
</script>

<div class="chart-container">
  <svg bind:this={svgElement}></svg>
</div>

<style>
  .chart-container {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    border-radius: 4px;
    border: 1px solid #ddd;
    padding: 1rem;
  }
</style>
