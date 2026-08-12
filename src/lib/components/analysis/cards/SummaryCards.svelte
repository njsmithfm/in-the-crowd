<script>
  let { totalShows, freeShows, yearsCovered, topBorough, topVenue } = $props();
</script>

<section class="summary-cards">
  <div class="summary-card">
    <span class="label">Total shows</span>
    <strong>{totalShows}</strong>
  </div>

  <div class="summary-card">
    <span class="label">Free shows</span>
    <strong>{freeShows}</strong>
  </div>

  <div class="summary-card">
    <span class="label">Years covered</span>
    <strong>{yearsCovered}</strong>
  </div>

  <div class="summary-card">
    <span class="label">Top borough</span>
    <strong>{topBorough}</strong>
  </div>

  <div class="summary-card">
    <span class="label">Top venue</span>
    <strong>{topVenue}</strong>
  </div>
</section>
