export async function runPipeline(opportunityId: string) {
  const res = await fetch(`/api/jobs/opportunity/${opportunityId}/run-pipeline`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
  });
  if (!res.ok) {
    throw new Error('Failed to run pipeline');
  }
  return await res.json();
}

export async function getJobStatus(taskId: string) {
  const res = await fetch(`/api/jobs/status/${taskId}`, {
    cache: 'no-store',
  });
  if (!res.ok) {
    throw new Error('Failed to get job status');
  }
  return await res.json();
}
