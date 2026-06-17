<script>
  import shows from "../../../public/data/shows.json";
  let { onSelectShow = null } = $props();

  const groupedByBorough = shows.reduce((acc, show) => {
    const borough = show.Borough;
    if (!acc[borough]) acc[borough] = [];
    acc[borough].push(show);
    return acc;
  }, {});

  const handleShowClick = (show) => {
    if (onSelectShow) {
      onSelectShow({
        artist: show.Artist,
        venue: show.Venue,
        date: show.Date,
        borough: show.Borough,
        free_show: show.Free_Show,
      });
    }
  };
</script>

<div class="map">
  {#each Object.entries(groupedByBorough) as [borough, boroughShows]}
    <div class="borough-section">
      <h2>{borough}</h2>
      <div class="shows-grid">
        {#each boroughShows as show}
          <button class="show-card" onclick={() => handleShowClick(show)}>
            <span class="artist">{show.Artist}</span>
            <span class="venue">{show.Venue}</span>
            {#if show.Free_Show}
              <span class="badge free">FREE</span>
            {/if}
          </button>
        {/each}
      </div>
    </div>
  {/each}
</div>

<style>
  .map {
    padding: 1rem;
  }

  .borough-section {
    margin-bottom: 2rem;
  }

  .shows-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }

  .show-card {
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    background: white;
    text-align: left;
    font-family: inherit;
    font-size: inherit;
  }

  .show-card:hover {
    background-color: #f5f5f5;
    border-color: #999;
  }

  .show-card:focus {
    outline: 2px solid #333;
    outline-offset: 2px;
  }

  .artist {
    font-weight: bold;
    margin-bottom: 0.5rem;
    display: block;
  }

  .badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 3px;
    font-size: 0.75rem;
    font-weight: bold;
    margin-top: 0.5rem;
  }

  .badge.free {
    background-color: #4caf50;
    color: white;
  }
</style>
