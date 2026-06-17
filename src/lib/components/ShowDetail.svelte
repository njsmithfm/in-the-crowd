<script>
  let { show = null, onClose } = $props();
</script>

<div class="detail-view">
  <div class="detail-content">
    <button class="close-btn" onclick={onClose}>✕</button>

    {#if show}
      <h2>{show.artist}</h2>

      <div class="show-details">
        <p class="venue">
          <strong>Venue:</strong>
          {show.venue}
        </p>
        <p class="date">
          <strong>Date:</strong>
          {new Date(show.date).toLocaleDateString()}
        </p>
        {#if show.description}
          <p class="description">
            <strong>Notes:</strong>
            {show.description}
          </p>
        {/if}
      </div>
    {/if}
  </div>
</div>

<style>
  .detail-view {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    overflow-y: auto;
  }

  .detail-content {
    background-color: white;
    border-radius: 8px;
    max-width: 800px;
    width: 90%;
    padding: 2rem;
    position: relative;
    max-height: 90vh;
    overflow-y: auto;
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #666;
    padding: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .close-btn:hover {
    color: #000;
  }

  .show-details {
    margin-top: 2rem;
  }

  h2 {
    margin-top: 0;
    font-size: 1.8rem;
  }

  .venue,
  .date,
  .description {
    margin: 0.5rem 0;
    line-height: 1.6;
  }

  .description {
    margin-top: 1rem;
    padding: 1rem;
    background-color: #f9f9f9;
    border-left: 3px solid #333;
  }
</style>
