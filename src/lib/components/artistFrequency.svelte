<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import shows from "../../../public/data/shows.json";

  let canvasEl;

  onMount(() => {
    if (!canvasEl) return;

    // Count shows by artist
    const artistCount = {};
    shows.forEach((show) => {
      artistCount[show.Artist] = (artistCount[show.Artist] || 0) + 1;
    });

    // Sort by count descending and take top 10
    const sorted = Object.entries(artistCount)
      .sort(([, a], [, b]) => b - a)
      .slice(0, 10);

    const ctx = canvasEl.getContext("2d");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: sorted.map(([artist]) => artist),
        datasets: [
          {
            label: "Shows",
            data: sorted.map(([, count]) => count),
            backgroundColor: "rgba(153, 102, 255, 0.6)",
            borderColor: "rgba(153, 102, 255, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: true,
            text: "Top 10 Artists",
            font: {
              size: 14,
              weight: "bold",
            },
          },
        },
        scales: {
          x: {
            beginAtZero: true,
            ticks: {
              stepSize: 1,
            },
          },
        },
      },
    });
  });
</script>

<div class="chart-container">
  <canvas bind:this={canvasEl}></canvas>
</div>

<style>
  .chart-container {
    position: relative;
    height: 300px;
    width: 100%;
    padding: 1rem;
    background-color: white;
    border-radius: 4px;
    border: 1px solid #ddd;
  }
</style>
