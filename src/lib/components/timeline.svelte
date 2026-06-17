<script>
  import shows from "../../../public/data/shows.json";
  let { onSelectShow } = $props();

  const groupedByYear = shows.reduce((acc, show) => {
    const year = show.Year;
    if (!acc[year]) acc[year] = [];
    acc[year].push(show);
    return acc;
  }, {});

  const handleShowClick = (show) => {
    onSelectShow({
      artist: show.Artist,
      venue: show.Venue,
      date: show.Date,
      borough: show.Borough,
      free_show: show.Free_Show,
    });
  };
</script>

<div class="timeline">
  {#each Object.entries(groupedByYear) as [year, yearShows]}
    <h2>{year}</h2>
    {#each yearShows as show}
      <button class="show-card" onclick={() => handleShowClick(show)}>
        <span class="artist">{show.Artist}</span>
        <span class="venue">{show.Venue}</span>
        {#if show.Free_Show}
          <span class="badge free">FREE</span>
        {/if}
      </button>
    {/each}
  {/each}
</div>

<style>
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

  .venue {
    display: block;
    color: #666;
    margin-bottom: 0.5rem;
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
