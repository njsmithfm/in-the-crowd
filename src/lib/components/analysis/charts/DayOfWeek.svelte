<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import { onMount } from "svelte";
  import shows from "../../../../../public/data/shows.json";
  import { boroughColors } from "../boroughColors.js";
  import * as d3 from "d3";

  let dayCounts = {};
  for (let show of shows) {
    const day = show.Day;
    if (!dayCounts[day]) {
      dayCounts[day] = { count: 0 };
    }
    dayCounts[day].count += 1;
  }
  console.log(dayCounts);

  let widthScale = d3.scaleLinear().domain([0, 50]).range([0, 500]);

  let svg;

  onMount(() => {
    d3.select(svg)
      .selectAll("rect")
      .data(Object.entries(dayCounts))
      .enter()
      .append("rect")
      .attr("height", 20)
      .attr("y", (d, i) => i * 25)
      .attr("fill", "blue")
      .attr("width", function (d) {
        console.log(d);
        return widthScale(d[1].count);
      });
  });
</script>

<ChartWrapper title="Days of the Week">
  <svg bind:this={svg} class="chart-svg"> </svg>
</ChartWrapper>
