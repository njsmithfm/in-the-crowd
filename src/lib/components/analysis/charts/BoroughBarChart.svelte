<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import ChartWrapper from "../ChartWrapper.svelte";
  import { boroughColors } from "../boroughColors.js";
  import shows from "../../../../../public/data/shows.json";
  let svg;

  onMount(() => {
    const width = 640;
    const height = 320;
    const margin = { top: 20, right: 20, bottom: 40, left: 40 };

    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const counts = Array.from(
      d3.rollup(
        shows,
        (items) => items.length,
        (show) => show.Borough,
      ),
      ([label, value]) => ({ label, value }),
    ).sort((a, b) => d3.descending(a.value, b.value));

    const x = d3
      .scaleBand()
      .domain(counts.map((d) => d.label))
      .range([0, innerWidth])
      .padding(0.2);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(counts, (d) => d.value) ?? 0])
      .nice()
      .range([innerHeight, 0]);

    const root = d3.select(svg);
    root.selectAll("*").remove();

    const g = root
      .attr("viewBox", `0 0 ${width} ${height}`)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    g.append("g")
      .attr("transform", `translate(0,${innerHeight})`)
      .call(d3.axisBottom(x))
      .selectAll("text")
      .attr("transform", "rotate(-25)")
      .style("text-anchor", "end");

    g.append("g").call(d3.axisLeft(y).ticks(4));

    g.selectAll("rect")
      .data(counts)
      .join("rect")
      .attr("x", (d) => x(d.label))
      .attr("y", (d) => y(d.value))
      .attr("width", x.bandwidth())
      .attr("height", (d) => innerHeight - y(d.value))
      .attr("fill", (d) => boroughColors[d.label] || "#111");
  });
</script>

<ChartWrapper title="Shows by Location">
  <svg bind:this={svg}></svg>
</ChartWrapper>
