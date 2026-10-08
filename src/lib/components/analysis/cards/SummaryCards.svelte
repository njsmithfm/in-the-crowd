<script>
  let { totalShows, freeShows, yearsCovered, topBorough, topVenue } = $props();
</script>

<div class="summary-grid">
  <div class="summary-card">
    <span class="label">
      <strong>{totalShows}</strong> total shows attended</span
    >
  </div>

  <div class="summary-card">
    <span class="label"><strong>{freeShows}</strong> free shows attended</span>
  </div>

  <div class="summary-card">
    <span class="label"><strong>{yearsCovered}</strong> years of data</span>
  </div>

  <div class="summary-card">
    <span class="label"
      ><strong>{topBorough}</strong> rocks the hardest (I saw shows here the most)</span
    >
  </div>

  <div class="summary-card">
    <span class="label"
      ><strong>{topVenue}</strong> is the top venue I've been to</span
    >
  </div>
</div>

<style>
  .summary-grid {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
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
    display: block;
    line-height: 1.3;
  }

  strong {
    font-size: 1.25rem;
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
