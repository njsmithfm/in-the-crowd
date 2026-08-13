<script>
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import BoroughBarChart from "$lib/components/analysis/charts/BoroughBarChart.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TopVenuesChart from "$lib/components/analysis/charts/TopVenuesChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";

  import shows from "../../../../public/data/shows.json";

  const sortedShows = [...shows].sort((a, b) => b.Show_Number - a.Show_Number);

  const boroughCounts = sortedShows.reduce((counts, show) => {
    counts[show.Borough] = (counts[show.Borough] ?? 0) + 1;
    return counts;
  }, {});

  const venueCounts = sortedShows.reduce((counts, show) => {
    counts[show.Venue] = (counts[show.Venue] ?? 0) + 1;
    return counts;
  }, {});

  const yearCounts = sortedShows.reduce((counts, show) => {
    counts[show.Year] = (counts[show.Year] ?? 0) + 1;
    return counts;
  }, {});

  const freeShowsByYear = sortedShows.reduce((counts, show) => {
    if (show.Free_Show) {
      counts[show.Year] = (counts[show.Year] ?? 0) + 1;
    }

    return counts;
  }, {});

  const totalShows = sortedShows.length;
  const freeShows = sortedShows.filter((show) => show.Free_Show).length;

  const yearsCovered = new Set(sortedShows.map((show) => show.Year)).size;
  const topBorough = boroughCounts[0]?.label ?? "N/A";
  const topVenue = venueCounts[0]?.label ?? "N/A";
  const stats = {
    totalShows,
    freeShows,
    yearsCovered,
    topBorough,
    topVenue,
  };
</script>

<div style="display: flex; height: 100vh;">
  <section class="analysis-dashboard">
    <div class="dashboard-grid">
      <div><SummaryCards {...stats} /></div>
      <!-- <div><BoroughBarChart /></div>
      <div><TopVenuesChart /></div>
      <div><FreeShowsChart /></div> -->

      <div><TimelineChart /></div>
    </div>
  </section>
  <!-- Explicitly pass the function -->
</div>

<style>
  .analysis-dashboard {
    margin: 2.5rem;
  }

  .dashboard-grid {
    display: grid;
    min-width: 100%;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 2fr;
  }
  .dashboard-grid div {
    margin: 1.5rem;
  }
</style>
