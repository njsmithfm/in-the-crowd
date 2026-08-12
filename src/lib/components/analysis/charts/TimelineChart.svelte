<script>
  import { onMount } from "svelte";
  import d3 from "d3";
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
      .scaleTime()
      .domain(d3.extent(data, (d) => d.date))
      .range([0, innerWidth]);

    const years = Array.from(new Set(data.map((d) => d.year))).sort();
    const y = d3
      .scalePoint()
      .domain(years)
      .range([innerHeight, 0])
      .padding(0.5);

    const simulation = d3
      .forceSimulation(data)
      .force("x", d3.forceX((d) => x(d.date)).strength(1))
      .force("y", d3.forceY((d) => y(d.year)).strength(0.6))
      .force("collide", d3.forceCollide(5))
      .stop();
  });
</script>

<BaseChartPanel title="Timeline" subtitle="(I rock through time)">
  <svg bind:this={svg} class="chart-svg"></svg>
</BaseChartPanel>
