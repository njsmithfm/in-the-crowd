<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import BaseChartPanel from "$lib/components/analysis/charts/BaseChartPanel.svelte";

  let { data = [] } = $props();
  let svg;

  onMount(() => {
    const width = 640;
    const height = 320;
    const margin = { top: 20, right: 20, bottom: 40, left: 40 };

    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const x = d3
      .scaleBand()
      .domain(data.map((d) => d.label))
      .range([0, innerWidth])
      .padding(0.2);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.value) ?? 0])
      .nice()
      .range([innerHeight, 0]);

    const root = d3.select(svg);
    root.selectAll("*").remove();

    const g = root
      .attr("viewBox", `0 0 ${width} ${height}`)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.selectAll("rect")
      .data(data)
      .join("rect")
      .attr("x", (d) => x(d.label))
      .attr("y", (d) => y(d.value))
      .attr("width", x.bandwidth())
      .attr("height", (d) => innerHeight - y(d.value))
      .attr("fill", "#111");
  });
</script>

<BaseChartPanel title="Venues" subtitle="Venues I've been to the most">
  <svg bind:this={svg} class="chart-svg"></svg>
</BaseChartPanel>
