<script>
  import { page } from "$app/stores";
  import PageHeader from "$lib/components/PageHeader.svelte";
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import BoroughBarChart from "$lib/components/analysis/charts/BoroughBarChart.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TopVenuesChart from "$lib/components/analysis/charts/TopVenuesChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";

  let { stats, boroughData, venueData, freeShowData, timelineData } = $props();
</script>

<div style="display: flex;  padding: 1rem; border-bottom: 1px solid #000;">
  <PageHeader />
</div>

<div style="display: flex; height: 100vh;">
  <div style="flex: 65%; border-right: 1px solid #000; padding: 1rem;">
    <section class="analysis-dashboard">
      <SummaryCards {...stats} />

      <div class="dashboard-grid">
        <TimelineChart data={timelineData} />
        <BoroughBarChart data={boroughData} />
        <TopVenuesChart data={venueData} />
        <FreeShowsChart data={freeShowData} />
      </div>
    </section>
    <!-- Explicitly pass the function -->
    <!-- <ShowsList onSelect={handleSelection} /> -->
  </div>

  <div style="flex: 35%; padding: 1rem;">
    <!-- Pass the object directly -->
    <!-- <ShowDetail show={selectedShow} onClose={() => (selectedShow = null)} /> -->
  </div>
</div>

<style>
</style>
