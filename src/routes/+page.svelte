<script>
  import Timeline from "$lib/components/Timeline.svelte";
  import Map from "$lib/components/Map.svelte";

  let activeView = $state("timeline");
</script>

<h1>In The Crowd</h1>

<div class="tabs">
  <button onclick={() => (activeView = "timeline")}>Timeline</button>
  <button onclick={() => (activeView = "map")}>Map</button>
</div>

{#if activeView === "timeline"}
  <Timeline />
{:else if activeView === "map"}
  <Map />
{/if}
