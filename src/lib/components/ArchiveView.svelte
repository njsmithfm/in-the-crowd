<script>
  import ShowsList from "$lib/components/ShowsList.svelte";
  import ShowDetail from "$lib/components/ShowDetail.svelte";

  let selectedShow = $state(null);

  const handleSelection = (showData) => {
    selectedShow = showData;
  };
</script>

<div class="archive-layout">
  <div class="archive-list-pane">
    {#if !selectedShow}
      <p class="mobile-select-prompt">Select a show!</p>
    {/if}
    <!-- Explicitly pass the function -->
    <ShowsList onSelect={handleSelection} />
  </div>

  <div class="archive-detail-pane" class:has-show={Boolean(selectedShow)}>
    <!-- Pass the object directly -->
    <ShowDetail show={selectedShow} onClose={() => (selectedShow = null)} />
  </div>
</div>

<style>
  .archive-layout {
    display: grid;
    grid-template-columns: minmax(0, 1.85fr) minmax(18rem, 1fr);
    height: calc(100dvh - 9rem);
    overflow: hidden;
  }

  .archive-list-pane,
  .archive-detail-pane {
    min-width: 0;
    min-height: 0;
    padding: clamp(0.75rem, 2vw, 1rem);
  }

  .archive-list-pane {
    border-right: 1px solid #000;
  }

  .archive-detail-pane {
    position: sticky;
    top: 0;
    align-self: start;
    max-height: calc(100vh - 9rem);
    overflow-y: auto;
  }

  .mobile-select-prompt {
    display: none;
  }

  @media (max-width: 700px) {
    .archive-layout {
      display: flex;
      height: calc(100dvh - 8rem);
      flex-direction: column;
    }

    .archive-list-pane {
      display: flex;
      flex: 1 1 auto;
      flex-direction: column;
      min-height: 0;
      overflow: hidden;
      border-right: 0;
      border-bottom: 1px solid #000;
    }

    .archive-detail-pane {
      display: none;
    }

    .archive-detail-pane.has-show {
      position: fixed;
      top: 50%;
      right: 1rem;
      left: 1rem;
      z-index: 1200;
      display: block;
      max-height: calc(100dvh - 2rem);
      overflow-y: auto;
      border: 1px solid #000;
      background: #fff;
      box-shadow: 0 0 0 100vmax rgba(0, 0, 0, 0.35);
      transform: translateY(-50%);
    }

    .mobile-select-prompt {
      margin: 0 0 0.5rem;
      color: #ff00d4;
      font-weight: bold;
    }
  }
</style>
