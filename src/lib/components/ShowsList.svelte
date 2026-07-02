<script>
  import shows from "../../../public/data/shows.json";
  const sortedShows = shows.sort((a, b) => b.Show_Number - a.Show_Number);
  // Ensure this name matches the parent's key
  let { onSelect } = $props();
</script>

<div class="shows-list-container">
  <!-- Fixed header that doesn't move -->
  <div class="fixed-header">
    <h2>Shows by Date</h2>

    <div
      class="column-header-row"
      style="border-bottom: 1px solid #000; padding: 10px 5px;"
    >
      <span>Gig</span>
      <span>Date</span>
      <span>Artist</span>
      <span>Venue</span>
      <span>Location</span>
      <span></span>
    </div>
  </div>

  <!-- Scrollable content that sits BELOW the header -->
  <div class="date-shows-scrolling-area">
    {#each sortedShows as show}
      <button
        onclick={() => {
          console.log("Successful New Artist Selection:", show.Artist);
          if (onSelect) {
            onSelect(show);
          } else {
            console.error("onSelect prop is missing!");
          }
        }}
      >
        <div class="show-data-row">
          <span class="col-gig">{show.Show_Number} </span>
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
          <span class="col-free-show">
            {#if show?.Free_Show == true}
              <div class="free-show">FREE</div>{/if}</span
          >
        </div>
      </button>
    {/each}
  </div>
</div>

<style>
  .fixed-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background-color: white;
    height: var(--header-total-height);
  }

  .date-shows-scrolling-area {
    margin-top: var(--header-total-height);
    max-height: calc(100vh - var(--header-total-height));
    overflow-y: auto;
  }
  button {
    padding: 0.5rem 1rem;
    border: none;
    text-align: left;
    width: 100%;
    background: #fff;
    border-top: 0.5px solid rgb(236, 9, 193, 0.25);
    border-bottom: 0.5px solid rgb(236, 9, 193, 0.25);
    text-align: left;
    cursor: pointer;
    margin: 0;
    padding: 3px;
  }

  button:hover {
    border-top: 0.5px solid rgb(236, 9, 193);
    border-bottom: 0.5px solid rgb(236, 9, 193);
  }
  .free-show {
    display: inline-block;
    border: 1px solid #000;
    color: #ec09c1;
    font-size: 0.7rem;
    padding: 1.5px 2px;
    margin-left: 5px;
    border-radius: 3px;
  }
</style>
