<script>
  import ChartWrapper from "../ChartWrapper.svelte";
  import shows from "../../../../../public/data/shows.json";
  import { boroughColors } from "../boroughColors.js";

  let venueCounts = {};
  for (let show of shows) {
    const venue = show.Venue.trim();
    if (!venueCounts[venue]) {
      venueCounts[venue] = { count: 0, borough: show.Borough.trim() };
    }
    venueCounts[venue].count += 1;
  }

  let counts = Object.entries(venueCounts)
    .map(([venue, { count, borough }]) => ({ label: venue, count, borough }))
    .sort((a, b) => b.count - a.count)
    .slice(0, 12);

  const barHeight = 40;
</script>

<ChartWrapper title="Top Venues">
  <svg viewBox="-150 0 700 500">
    {#each counts as { label, count, borough }, i}
      <rect
        x={120}
        y={30 + i * barHeight}
        width={count * 10}
        height={barHeight - 5}
        fill={boroughColors[borough] || "#111"}
      />
      <text
        x={115}
        y={30 + i * barHeight + barHeight - 10}
        font-size="16"
        text-anchor="end"
      >
        {label}
      </text>
      <text
        x={125 + count * 10}
        y={30 + i * barHeight + barHeight - 10}
        font-size="16"
      >
        {count}
      </text>
    {/each}
  </svg>
</ChartWrapper>
