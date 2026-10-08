<script>
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";
  import DayOfWeek from "$lib/components/analysis/charts/DayOfWeek.svelte";
  import BoroughMap from "$lib/components/analysis/charts/BoroughMap.svelte";
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
  <SummaryCards {...stats} />
  <div class="dashboard-grid">
    <div class="timeline"><TimelineChart /></div>
    <div class="free-shows"><FreeShowsChart /></div>
    <div class="day-of-week"><DayOfWeek /></div>
    <div class="borough-map"><BoroughMap /></div>
  </div>
</section>

<style>
  .analysis-dashboard {
    box-sizing: border-box;
    width: min(100%, 1600px);
    margin: 0 auto;
    padding: clamp(1rem, 3vw, 2.5rem);
  }
  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: clamp(1rem, 2vw, 1.5rem);
  }
  .dashboard-grid > div {
    min-width: 0;
  }

  .timeline {
    grid-column: 1 / -1;
  }

  .free-shows {
    grid-column: 1;
  }

  .day-of-week {
    grid-column: 2;
  }

  .borough-map {
    grid-column: 1 / -1;
  }

  @media (min-width: 1100px) {
    .analysis-dashboard {
      padding: 1rem 2rem;
    }

    .dashboard-grid {
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1.35fr);
      grid-template-rows: auto auto;
      gap: 1rem;
    }

    :global(.summary-grid) {
      margin-bottom: 0.75rem;
    }

    .timeline {
      grid-column: 1 / 3;
    }

    .borough-map {
      grid-column: 3;
      grid-row: 1 / 3;
    }

    .borough-map :global(.chart-panel-body) {
      align-items: flex-start;
      padding-top: 0.25rem;
    }
  }

  @media (max-width: 600px) {
    .dashboard-grid {
      grid-template-columns: minmax(0, 1fr);
    }

    .timeline,
    .free-shows,
    .day-of-week,
    .borough-map {
      grid-column: 1;
    }
  }
</style>
