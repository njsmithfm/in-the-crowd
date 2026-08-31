<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import shows from "../../../../../public/data/shows.json";

  // Step 1: Count shows at each venue
  let venueCounts = {};
  for (let show of shows) {
    if (!venueCounts[show.Venue]) {
      venueCounts[show.Venue] = 0;
    }
    venueCounts[show.Venue] += 1;
  }

  // Step 2: Convert to array format [venueName, count]
  let venueEntries = [];
  for (let venue in venueCounts) {
    venueEntries.push([venue, venueCounts[venue]]);
  }

  // Step 3: Sort by highest count first
  venueEntries.sort((a, b) => b[1] - a[1]);

  // Step 4: Take top 12 only
  let topVenues = venueEntries.slice(0, 12);

  // Step 5: Format as {label, value} for easier use
  let counts = [];
  for (let [venue, count] of topVenues) {
    counts.push({ label: venue, value: count });
  }

  const barHeight = 40;
</script>

<ChartWrapper title="Top Venues">
  <svg viewBox="0 0 700 500">
    {#each counts as { label, value }, i}
      <rect
        x={20 + i * 50}
        y={30 + i * barHeight}
        width={40}
        height={barHeight - 5}
        fill="#6d4aff"
      />
      <text x={40 + i * 50} y={30 + i * barHeight + barHeight} font-size="10"
        >{label}</text
      >
      <text x={40 + i * 50} y={25 + i * barHeight} font-size="10">{value}</text>
    {/each}
  </svg>
</ChartWrapper>
