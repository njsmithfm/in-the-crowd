<script>
  let { show, onClose } = $props();
  let selectedImageIndex = $state(0);
</script>

<div style="border: 5px solid #ff00d4; padding: 20px; background: white;">
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

    <!-- Media Display -->
    <div style="margin: 20px 0;">
      {#if show.media?.video}
        <video
          width="100%"
          height="auto"
          controls
          style="margin-bottom: 15px; background: #000;"
        >
          <source src={show.media.video} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      {/if}

      {#if show.media?.images && show.media.images.length > 0}
        <div>
          <img
            src={show.media.images[selectedImageIndex]}
            alt={show.Artist}
            style="max-width: 100%; height: auto; margin-bottom: 10px;"
          />
          {#if show.media.images.length > 1}
            <div
              style="display: flex; gap: 10px; justify-content: center; margin-top: 10px;"
            >
              {#each show.media.images as _, index}
                <button
                  onclick={() => (selectedImageIndex = index)}
                  style="padding: 5px 10px; background: {index ===
                  selectedImageIndex
                    ? '#ff00d4'
                    : '#f0f0f0'}; color: {index === selectedImageIndex
                    ? '#fff'
                    : '#000'}; border: 1px solid #ff00d4; cursor: pointer;"
                >
                  {index + 1}
                </button>
              {/each}
            </div>
          {/if}
        </div>
      {/if}
      {#if show?.Notes}
        <p style="margin:0; "><i>Notes:</i></p>
        <div class="show-notes">{show.Notes}</div>
      {/if}
      <!-- Fallback for old single mediaPath format (backwards compat) -->
      {#if !show.media && show.media}
        <img
          src={show.mediaPath}
          alt={show.Artist}
          style="max-width: 100%; height: auto;"
        />
      {/if}
    </div>
  {:else}
    <p style="color: #ff00d4; font-weight: bold;">Select a show from left!</p>
  {/if}

  <button onclick={onClose}>Close</button>
</div>

<style>
  .show-notes {
    margin: 0.75rem;
  }
</style>
