<script>
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import BoroughBarChart from "$lib/components/analysis/charts/BoroughBarChart.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TopVenuesChart from "$lib/components/analysis/charts/TopVenuesChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";

  let { stats, boroughData, venueData, freeShowData, timelineData } = $props();
</script>

<section class="analysis-dashboard">
  <SummaryCards {...stats} />

  <div class="dashboard-grid">
    <TimelineChart data={timelineData} />
    <BoroughBarChart data={boroughData} />
    <TopVenuesChart data={venueData} />
    <FreeShowsChart data={freeShowData} />
  </div>
</section>
