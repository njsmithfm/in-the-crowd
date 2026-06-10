<script>
  import Timeline from "$lib/components/Timeline.svelte";
  import Map from "$lib/components/Map.svelte";

  let activeView = "timeline";
</script>

<h1>In The Crowd</h1>

<div class="tabs">
  <button on:click={() => (activeView = "timeline")}>Timeline</button>
  <button on:click={() => (activeView = "map")}>Map</button>
</div>

{#if activeView === "timeline"}
  <Timeline />
{:else if activeView === "map"}
  <Map />
{/if}
