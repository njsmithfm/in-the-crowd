<script>
  import shows from "../../../public/data/shows.json";

  const groupedByYear = shows.reduce((acc, show) => {
    const year = show.Year;
    if (!acc[year]) acc[year] = [];
    acc[year].push(show);
    return acc;
  }, {});
</script>

<div class="timeline">
  {#each Object.entries(groupedByYear) as [year, yearShows]}
    <h2>{year}</h2>
    {#each yearShows as show}
      <div class="show-card">
        <span class="artist">{show.Artist}</span>
        <span class="venue">{show.Venue}</span>
        <span class="borough">{show.Borough}</span>
        {#if show.Free_Show}
          <span class="badge free">FREE</span>
        {/if}
      </div>
    {/each}
  {/each}
</div>
