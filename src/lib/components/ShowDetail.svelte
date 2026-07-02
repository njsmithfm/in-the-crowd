<script>
  let { show, onClose } = $props();
</script>

<div style="border: 5px solid #EC09C1; padding: 20px; background: white;">
  <!-- Check if 'show' exists first -->
  {#if show}
    <h1>{show.Artist}</h1>
    <p>{show.Venue} in {show.Borough}</p>
    <p>
      {new Date(show.Date).toLocaleDateString("en-gb", {
        day: "numeric",
        month: "long",
        year: "numeric",
      })}
    </p>
    {#if show?.Notes}
      <p><strong><i>Notes:</i></strong> {show.Notes}</p>
    {/if}
    {#if show?.Image_Path}
      <img src={show.Image_Path} alt={show.Artist} />
    {/if}
  {:else}
    <p style="color: #EC09C1; font-weight: bold;">
      Select a show to view details
    </p>
  {/if}

  <button onclick={onClose}>Close</button>
</div>
