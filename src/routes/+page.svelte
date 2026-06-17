<script>
  import Timeline from "$lib/components/Timeline.svelte";
  import Map from "$lib/components/Map.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";
  import "@fontsource/public-sans"; // Defaults to weight 400
  import "@fontsource/public-sans/400.css"; // Specify weight
  import "@fontsource/public-sans/400-italic.css"; // Specify weight and style

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

<style>
  * {
    font-family: "Public Sans", sans-serif;
  }
</style>
