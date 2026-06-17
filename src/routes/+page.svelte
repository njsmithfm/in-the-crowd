<script>
  import Timeline from "$lib/components/Timeline.svelte";
  import Map from "$lib/components/Map.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";

  let activeView = $state("timeline");
  let selectedShow = $state(null);
</script>

<h1>In The Crowd</h1>

<div class="tabs">
  <button onclick={() => (activeView = "timeline")}>Timeline</button>
  <button onclick={() => (activeView = "map")}>Map</button>
</div>

{#if activeView === "timeline"}
  <Timeline onSelectShow={(show) => (selectedShow = show)} />
{:else if activeView === "map"}
  <Map onSelectShow={(show) => (selectedShow = show)} />
{/if}

{#if selectedShow}
  <ShowDetail show={selectedShow} onClose={() => (selectedShow = null)} />
{/if}
