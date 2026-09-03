<script>
  let { totalShows, freeShows, yearsCovered, topBorough, topVenue } = $props();
</script>

<div class="summary-card">
  <span class="label"> <strong>{totalShows}</strong> total shows</span>
</div>

<div class="summary-card">
  <span class="label"><strong>{freeShows}</strong> free shows</span>
</div>

<div class="summary-card">
  <span class="label"><strong>{yearsCovered}</strong> years of data</span>
</div>

<div class="summary-card">
  <span class="label"><strong>{topBorough}</strong> rocks the hardest</span>
</div>

<div class="summary-card">
  <span class="label"><strong>{topVenue}</strong> was the top venue</span>
</div>
