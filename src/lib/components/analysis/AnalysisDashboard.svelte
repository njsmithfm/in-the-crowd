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

  const boroughData = Object.entries(boroughCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value);

  const venueData = Object.entries(venueCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value)
    .slice(0, 5);

  const timelineData = Object.entries(yearCounts)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => Number(a.label) - Number(b.label));

  const freeShowData = Object.entries(freeShowsByYear)
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => Number(a.label) - Number(b.label));

  const totalShows = sortedShows.length;
  const freeShows = sortedShows.filter((show) => show.Free_Show).length;

  const yearsCovered = new Set(sortedShows.map((show) => show.Year)).size;
  const topBorough = boroughData[0]?.label ?? "N/A";
  const topVenue = venueData[0]?.label ?? "N/A";
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
      <div><TimelineChart data={timelineData} /></div>
      <div><BoroughBarChart data={boroughData} /></div>
      <div><TopVenuesChart data={venueData} /></div>
      <div><FreeShowsChart data={freeShowData} /></div>
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
