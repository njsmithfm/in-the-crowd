<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import { onMount } from "svelte";
  import shows from "../../../../../public/data/shows.json";
  import * as d3 from "d3";

  let dayCounts = {};
  for (let show of shows) {
    const day = show.Day;
    if (!dayCounts[day]) {
      dayCounts[day] = { count: 0 };
    }
    dayCounts[day].count += 1;
  }
  let daysArray = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];
  let xScale = d3.scaleLinear().domain([0, 50]).range([0, 250]);
  let yScale = d3.scaleBand().domain(daysArray).range([0, 150]).padding(1);

  let svg;
  let width = 640;
  let height = 200;

  onMount(() => {
    const chart = d3.select(svg).attr("width", "100%").attr("height", "100%");
    chart
      .selectAll("rect")
      .data(Object.entries(dayCounts)) // bind the data
      .enter()
      .append("rect")
      .attr("width", function (d) {
        return xScale(d[1].count); // widthScale is an array and count is the key needed in the dayCounts object to return the counted values
      })
      .attr("height", 15)
      .attr("x", 0)
      .attr("y", function (d) {
        return yScale(d[0]);
      })
      .attr("fill", "#ff00d440")
      .attr("stroke", "black");

    let yAxis = d3.axisLeft(yScale);
    chart.append("g").call(yAxis);

    let xAxis = d3.axisBottom(xScale);
    chart
      .append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);
  });
</script>

<ChartWrapper title="Days of the Week" subtitle="counts of days">
  <svg
    bind:this={svg}
    viewBox={`-100 0 ${width + 20} ${height + 30}`}
    width="100%"
    height="100%"
  >
  </svg>
</ChartWrapper>
