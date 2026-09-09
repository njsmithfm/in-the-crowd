<script>
  let { totalShows, freeShows, yearsCovered, topBorough, topVenue } = $props();
</script>

<div class="summary-card">
  <span class="label"> <strong>{totalShows}</strong> total shows attended</span>
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
