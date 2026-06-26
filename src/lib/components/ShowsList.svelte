<script>
  import shows from "../../../public/data/shows.json";

  // Ensure this name matches the parent's key
  let { onSelect } = $props();
</script>

<div class="shows-list-container">
  <h2>Shows by Date</h2>

  <div class="date-shows">
    {#each shows as show}
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
        <div class="show-list-item">
          <strong>{show.Artist}</strong> at {show.Venue}
        </div>
      </button>{/each}
  </div>
</div>
