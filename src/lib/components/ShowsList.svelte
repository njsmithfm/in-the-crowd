<script>
  import shows from "../../../public/data/shows.json";

  let { selectedArtist = null, onSelectArtist } = $props();

  // Group shows by date
  const groupedByDate = shows.reduce((acc, show) => {
    const date = new Date(show.Date).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    if (!acc[date]) acc[date] = [];
    acc[date].push(show);
    return acc;
  }, {});

  const sortedDates = Object.keys(groupedByDate).sort(
    (a, b) => new Date(b) - new Date(a),
  );
</script>

<div class="shows-list-container">
  <h2>Shows by Date</h2>
  <div class="shows-list">
    {#each sortedDates as date}
      <div class="date-group">
        <h3 class="date-header">{date}</h3>
        <div class="date-shows">
          {#each groupedByDate[date] as show}
            <button
              class="show-button"
              class:active={selectedArtist === show.Artist}
              onclick={() => onSelectArtist(show.Artist)}
            >
              <span class="artist-name">{show.Artist}</span>
              <span class="venue-name">{show.Venue}</span>
              {#if show.Free_Show}
                <span class="badge">FREE</span>
              {/if}
            </button>
          {/each}
        </div>
      </div>
    {/each}
  </div>
</div>

<style>
  .shows-list-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    padding: 1rem;
    overflow-y: auto;
    background-color: #fafafa;
  }

  h2 {
    margin-top: 0;
    margin-bottom: 1.5rem;
    font-size: 1.3rem;
    font-weight: 600;
  }

  .shows-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .date-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .date-header {
    margin: 0;
    font-size: 0.95rem;
    font-weight: 700;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 0.5rem 0;
    border-bottom: 2px solid #ddd;
  }

  .date-shows {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .show-button {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
    padding: 0.75rem 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: white;
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
  }

  .show-button:hover {
    background-color: #f0f0f0;
    border-color: #999;
  }

  .show-button.active {
    background-color: #333;
    border-color: #333;
    color: white;
  }

  .artist-name {
    font-weight: 600;
    font-size: 0.95rem;
  }

  .venue-name {
    font-size: 0.85rem;
    color: #666;
  }

  .show-button.active .venue-name {
    color: #ccc;
  }

  .badge {
    display: inline-block;
    padding: 0.2rem 0.4rem;
    background-color: #4caf50;
    color: white;
    border-radius: 2px;
    font-size: 0.7rem;
    font-weight: bold;
    margin-top: 0.25rem;
  }
</style>
