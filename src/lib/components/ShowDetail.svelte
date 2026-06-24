<script>
  let { show, onClose } = $props();
</script>

<div style="border: 5px solid #EC09C1; padding: 20px; background: white;">
  <!-- Check if 'show' exists first -->
  {#if show}
    <h1>{show.Artist}</h1>
    <p>{show.Venue}</p>
    <p>
      {new Date(show.Date).toLocaleDateString("en-gb", {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric",
      })}
    </p>
    {#if show.Notes}
      <p><strong><i>Notes:</i></strong> {show.Notes}</p>
    {/if}
  {:else}
    <p style="color: #EC09C1; font-weight: bold;">
      Select a show to view details
    </p>
  {/if}

  <button onclick={onClose} style="margin-top: 10px;">Close</button>
</div>
