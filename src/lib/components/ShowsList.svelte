<script>
  import shows from "../../../public/data/shows.json";

  const sortedShows = [...shows].sort((a, b) => b.Show_Number - a.Show_Number);

  const groupShows = (showList) =>
    Object.values(
      showList.reduce((groups, show) => {
        const key = show.Bill_ID;
        (groups[key] ??= []).push(show);
        return groups;
      }, {}),
    ).sort((a, b) => b[0].Show_Number - a[0].Show_Number);

  const groupedShows = groupShows(sortedShows);

  let searchQuery = $state("");

  const visibleGroupedShows = () => {
    const normalizedQuery = searchQuery.trim().toLowerCase();

    if (!normalizedQuery) {
      return groupedShows;
    }

    const filteredShows = sortedShows.filter((show) =>
      String(show.Artist ?? "")
        .toLowerCase()
        .includes(normalizedQuery),
    );

    return groupShows(filteredShows);
  };

  let { onSelect } = $props();
</script>

<div class="shows-list-container">
  <!-- Fixed header that doesn't move -->
  <div class="fixed-header">
    <label class="search-bar" for="artist-search">
      <input
        id="artist-search"
        type="search"
        bind:value={searchQuery}
        placeholder="Search by artist!"
      />
    </label>
    <div
      class="column-header-row"
      style="border-bottom: 1px solid #000; padding: 10px 5px;"
    >
      <span>Gig</span>
      <span>Date</span>
      <span>Artist</span>
      <span>Venue</span>
      <span>Location</span>
      <span>¿Gratis?</span>
      <span></span>
    </div>
  </div>

  <!-- Scrollable content that sits BELOW the header -->
  <div class="date-shows-scrolling-area">
    {#each visibleGroupedShows() as billShows}
      <div class="bill-group">
        {#each billShows as show}
          <button onclick={() => onSelect?.(show)}>
            <div class="show-data-row">
              <span class="col-gig">{show.Show_Number}</span>
              <span class="col-date"
                >{new Date(show.Date).toLocaleDateString("en-gb", {
                  day: "numeric",
                  month: "long",
                  year: "numeric",
                })}</span
              >
              <span class="col-artist"><strong>{show.Artist}</strong></span>
              <span class="col-venue">{show.Venue}</span>
              <span class="col-borough">{show.Borough}</span>
              {#if show.Free_Show}
                <span class="col-free-show"
                  ><div class="free-show">FREE</div></span
                >
              {/if}
            </div>
          </button>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  .shows-list-container {
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  .fixed-header {
    background-color: white;
    flex: 0 0 auto;
    z-index: 100;
    padding-bottom: 0.5rem;
  }

  .search-bar {
    display: grid;
    gap: 0.35rem;
    margin-bottom: 0.75rem;
  }

  .search-bar input {
    width: 100%;
    border: 3px solid rgba(255, 0, 212, 0.5);
    padding: 0.55rem 0.75rem;
    background: #fff;
  }
  .search-bar input:focus {
    border: 3px solid rgb(255, 0, 212);
    outline: none;
  }

  .date-shows-scrolling-area {
    flex: 1 1 auto;
    overflow-y: auto;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    text-align: left;
    width: 100%;
    background: #fff;
    border-top: 0.5px solid rgba(255, 0, 212, 0.25);
    border-bottom: 0.5px solid rgba(255, 0, 212, 0.25);
    cursor: pointer;
    margin: 0;
    padding: 3px;
  }
  button:hover {
    border-top: 0.5px solid rgb(255, 0, 212);
    border-bottom: 0.5px solid #ff00d4;
  }

  .free-show {
    display: inline-block;
    border: 1px solid #000;
    color: rgb(255, 0, 212);
    font-size: 0.7rem;
    padding: 1.5px 2px;
    margin-left: 5px;
    border-radius: 3px;
  }
</style>
