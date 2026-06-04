<script lang>
  import { onMount } from "svelte";
  let shows = [];
  let loading = true;

  onMount(async () => {
    try {
      const res = await fetch("/data/shows.json");
      shows = await res.json();
    } catch (err) {
      console.error("Failed to load shows:", err);
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p>Loading shows...</p>
{:else}
  <p>{shows.length} shows loaded.</p>
  <!-- Debug: show first concert-->
  <pre>{JSON.stringify(shows[0], null, 2)}</pre>
{/if}
