<script>
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import BoroughBarChart from "$lib/components/analysis/charts/BoroughBarChart.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TopVenuesChart from "$lib/components/analysis/charts/TopVenuesChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";
  import DayOfWeek from "$lib/components/analysis/charts/DayOfWeek.svelte";

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
  console.log(boroughCounts);
  const topBorough = Object.keys(boroughCounts).reduce((a, b) =>
    boroughCounts[a] > boroughCounts[b] ? a : b,
  );
  const topVenue = Object.keys(venueCounts).reduce((a, b) =>
    venueCounts[a] > venueCounts[b] ? a : b,
  );
  const stats = {
    totalShows,
    freeShows,
    yearsCovered,
    topBorough,
    topVenue,
  };
</script>

<section class="analysis-dashboard">
  <div class="dashboard-grid">
    <div>
      <h2>Quick Stats</h2>
      <SummaryCards {...stats} />
    </div>
    <div><BoroughBarChart /></div>
    <div><TopVenuesChart /></div>
    <div><FreeShowsChart /></div>
    <div><TimelineChart /></div>
    <div><DayOfWeek /></div>
  </div>
</section>

<style>
  .analysis-dashboard {
    margin: 2.5rem;
    width: calc(100% - 5rem); /* account for margins */
    height: calc(100vh - 5rem);
  }

  .dashboard-grid {
    display: grid;

    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .dashboard-grid div {
    margin: 1.5rem;
    padding: 1rem;
    border: solid 2px;
    border-radius: 5px;
    border-color: #ff00d4;
  }
</style>
