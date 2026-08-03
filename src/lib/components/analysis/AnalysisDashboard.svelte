<script>
  import SummaryCards from "$lib/components/analysis/cards/SummaryCards.svelte";
  import BoroughBarChart from "$lib/components/analysis/charts/BoroughBarChart.svelte";
  import FreeShowsChart from "$lib/components/analysis/charts/FreeShowsChart.svelte";
  import TopVenuesChart from "$lib/components/analysis/charts/TopVenuesChart.svelte";
  import TimelineChart from "$lib/components/analysis/charts/TimelineChart.svelte";

  let { stats, boroughData, venueData, freeShowData, timelineData } = $props();
</script>

<div style="display: flex;  padding: 1rem; border-bottom: 1px solid #000;">
  <h1>
    <a href="/" target="_self" style="text-decoration: none; color: black; ;"
      >Archive</a
    >
    &
    <a
      href="./analysis"
      target="_self"
      style="text-decoration: none; color: black;">Analysis</a
    >
  </h1>
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
  .fixed-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background-color: white;
    height: var(--header-total-height);
  }

  .date-shows-scrolling-area {
    margin-top: var(--header-total-height);
    max-height: calc(100vh - var(--header-total-height));
    overflow-y: auto;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    text-align: left;
    width: 100%;
    background: #fff;
    border-top: 0.5px solid rgb(236, 9, 193, 0.25);
    border-bottom: 0.5px solid rgb(236, 9, 193, 0.25);
    cursor: pointer;
    margin: 0;
    padding: 3px;
  }
  button:hover {
    border-top: 0.5px solid #ec09c1;
    border-bottom: 0.5px solid #ec09c1;
  }

  .free-show {
    display: inline-block;
    border: 1px solid #000;
    color: #ec09c1;
    font-size: 0.7rem;
    padding: 1.5px 2px;
    margin-left: 5px;
    border-radius: 3px;
  }
</style>
