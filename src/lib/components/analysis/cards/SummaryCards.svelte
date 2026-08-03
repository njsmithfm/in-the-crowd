<script>
  let {
    totalShows,
    freeShows,
    showsWithNotes,
    yearsCovered,
    topBorough,
    topVenue,
  } = $props();
</script>

<section class="summary-cards">
  <article class="summary-card">
    <span class="label">Total shows</span>
    <strong>{totalShows}</strong>
  </article>

  <article class="summary-card">
    <span class="label">Free shows</span>
    <strong>{freeShows}</strong>
  </article>

  <article class="summary-card">
    <span class="label">Shows with notes</span>
    <strong>{showsWithNotes}</strong>
  </article>

  <article class="summary-card">
    <span class="label">Years covered</span>
    <strong>{yearsCovered}</strong>
  </article>

  <article class="summary-card">
    <span class="label">Top borough</span>
    <strong>{topBorough}</strong>
  </article>

  <article class="summary-card">
    <span class="label">Top venue</span>
    <strong>{topVenue}</strong>
  </article>
</section>
