<script>
  import AudioReactiveTitle from "./AudioReactiveTitle.svelte";
  import shows from "../../../public/data/shows.json";

  let { artistName = null, onClose } = $props();

  let artistShows = $derived(
    artistName
      ? shows
          .filter((show) => show.Artist === artistName)
          .sort((a, b) => new Date(b.Date) - new Date(a.Date))
      : [],
  );

  let artistNotes =
    shows.find((show) => show.Artist === artistName)?.Notes ||
    "No notes available.";

  let artistFrequency = artistShows.length;
</script>

<div class="detail-panel">
  <button class="close-btn" onclick={onClose}>✕</button>

  {#if AudioReactiveTitle !== ""}
    <AudioReactiveTitle {artistName} />
  {:else}
    <h2>{artistName}</h2>
  {/if}

  <div class="artist-info">
    {#if artistNotes?.length > 0}
      <h3>Notes</h3>
      <div class="notes">
        {artistNotes}
      </div>
    {/if}

    {#if artistFrequency >= 1}
      <h3>Other shows by {artistName}</h3>
      {#each artistShows as show}
        <div class="show-item">
          <span class="show-date">
            {new Date(show.Date).toLocaleDateString()}
          </span>
          <span class="show-venue">{show.Venue}</span>
          {#if show.Free_Show}
            <span class="badge-free">FREE</span>
          {/if}
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  .detail-panel {
    display: flex;
    flex-direction: column;
    height: 100%;
    background-color: white;
    border-left: 1px solid #ddd;
    overflow-y: auto;
    position: relative;
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
    z-index: 10;
  }

  .close-btn:hover {
    color: #000;
  }

  .artist-info {
    padding: 2rem 1.5rem;
    flex: 1;
  }

  h3 {
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    font-size: 1.1rem;
    font-weight: 600;
  }

  .shows-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .show-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem;
    background-color: #f9f9f9;
    border-radius: 4px;
    font-size: 0.95rem;
  }

  .show-date {
    font-weight: 600;
    color: #333;
    min-width: 90px;
  }

  .show-venue {
    flex: 1;
    color: #666;
  }

  .badge-free {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    background-color: #ec09c1;
    color: white;
    border-radius: 3px;
    font-size: 0.75rem;
    font-weight: bold;
  }

  .notes {
    padding: 1rem;
    background-color: #f9f9f9;
    border-left: 3px solid #333;
    line-height: 1.6;
    color: #555;
  }
</style>
