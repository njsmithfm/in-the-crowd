<script>
  let { totalShows, freeShows, yearsCovered, topBorough, topVenue, topDay } =
    $props();
</script>

<div class="summary-grid">
  <div class="summary-card">
    <span class="label"
      >I've got <strong>{yearsCovered}</strong> years of data here</span
    >
  </div>
  <div class="summary-card">
    <span class="label"
      >logging <strong>{totalShows}</strong> shows I've attended</span
    >
  </div>

  <div class="summary-card">
    <span class="label">mostly on <strong>{topDay}s</strong></span>
  </div>
  <div class="summary-card">
    <span class="label"
      >and <strong>{freeShows}</strong> of those shows were free</span
    >
  </div>
  <div class="summary-card">
    <span class="label">mostly in <strong>{topBorough}</strong> </span>
  </div>

  <div class="summary-card">
    <span class="label"
      >and <strong>{topVenue}</strong>is my most-visited venue</span
    >
  </div>
</div>

<style>
  .summary-grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    gap: 0.75rem;
    margin-bottom: clamp(1rem, 2vw, 1.5rem);
  }

  .summary-card {
    min-width: 0;
    padding: 0.9rem 1rem;
    border: 1px solid #000;
    background: #fff;
  }

  .label {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    line-height: 1.3;
  }

  strong {
    font-size: 1.15rem;
  }

  @media (max-width: 1000px) {
    .summary-grid {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }
  }

  @media (max-width: 600px) {
    .summary-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .summary-card {
      padding: 0.75rem;
      font-size: 0.9rem;
    }

    strong {
      font-size: 1.1rem;
    }
  }
</style>
