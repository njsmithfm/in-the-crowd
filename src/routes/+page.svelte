<script>
  import Timeline from "$lib/components/Timeline.svelte";
  import Map from "$lib/components/Map.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";
  import ShowsList from "$lib/components/ShowsList.svelte";
  import VenueFrequency from "$lib/components/venueFrequency.svelte";
  import ArtistFrequency from "$lib/components/artistFrequency.svelte";
  import "@fontsource/public-sans";
  import "@fontsource/public-sans/400.css";
  import "@fontsource/public-sans/400-italic.css";

  let activeView = $state("artists");
  let selectedArtist = $state(null);
</script>

<div class="container">
  <header>
    <h1>In The Crowd</h1>
    <nav class="nav-tabs">
      <button
        class="nav-tab"
        class:active={activeView === "artists"}
        onclick={() => (activeView = "artists")}
      >
        Artists
      </button>
      <button
        class="nav-tab"
        class:active={activeView === "analysis"}
        onclick={() => (activeView = "analysis")}
      >
        Analysis
      </button>
    </nav>
  </header>

  <main>
    {#if activeView === "artists"}
      <div class="split-pane">
        <div class="pane left">
          <ShowsList
            {selectedArtist}
            onSelectArtist={(artist) => (selectedArtist = artist)}
          />
        </div>
        <div class="pane right">
          {#if selectedArtist}
            <ShowDetail
              artistName={selectedArtist}
              onClose={() => (selectedArtist = null)}
            />
          {:else}
            <div class="placeholder">
              <p>Select an artist to view details</p>
            </div>
          {/if}
        </div>
      </div>
    {:else if activeView === "analysis"}
      <div class="analysis-grid">
        <div class="analysis-left">
          <Timeline />
          <VenueFrequency />
        </div>
        <div class="analysis-right">
          <Map />
        </div>
      </div>
    {/if}
  </main>
</div>

<style>
  :global(*) {
    font-family: "Public Sans", sans-serif;
  }

  .container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
    background-color: #fff;
  }

  header {
    padding: 1rem 2rem;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
  }

  h1 {
    margin: 0 0 1rem 0;
    font-size: 2rem;
    font-weight: 700;
  }

  .nav-tabs {
    display: flex;
    gap: 1rem;
    margin: 0;
  }

  .nav-tab {
    padding: 0.5rem 1rem;
    border: none;
    background: none;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    color: #666;
    border-bottom: 3px solid transparent;
    transition: all 0.2s;
  }

  .nav-tab:hover {
    color: #000;
  }

  .nav-tab.active {
    color: #000;
    border-bottom-color: #000;
  }

  main {
    flex: 1;
    overflow: hidden;
  }

  .split-pane {
    display: grid;
    grid-template-columns: 65% 35%;
    height: 100%;
    gap: 0;
  }

  .pane {
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  .pane.left {
    border-right: 1px solid #ddd;
  }

  .pane.right {
    position: relative;
  }

  .placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #999;
    font-size: 1.1rem;
  }

  .analysis-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    height: 100%;
    gap: 1rem;
    padding: 1rem;
    overflow: auto;
  }

  .analysis-left {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .analysis-right {
    display: flex;
    flex-direction: column;
  }
</style>
