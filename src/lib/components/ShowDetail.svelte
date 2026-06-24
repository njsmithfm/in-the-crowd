<script>
  let { show, onClose } = $props();
</script>

<div style="border: 5px solid red; padding: 20px; background: white;">
  <!-- Always render this container -->
  <h2 style="color: black;">DEBUG PANEL</h2>

  <!-- Check if 'show' exists first -->
  {#if show}
    <p style="color: green; font-weight: bold;">SHOW IS PRESENT!</p>
    <h1>{show.Artist}</h1>
    <p>Venue: {show.Venue}</p>
    <p>Date: {show.Date}</p>
    <p>Notes: {show.Notes}</p>
    Fallback if properties are undefined
    <!-- <pre>{JSON.stringify(show, null, 2)}</pre> -->
  {:else}
    <p style="color: red; font-weight: bold;">SHOW IS NULL/UNDEFINED</p>
  {/if}

  <button onclick={onClose} style="margin-top: 10px;">Close</button>
</div>
