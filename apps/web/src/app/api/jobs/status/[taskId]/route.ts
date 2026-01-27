import { NextResponse } from 'next/server';

// Proxy job status request to the backend API
export async function GET(
  request: Request,            
  { params }: { params: { taskId: string } }
) {
  const apiBase =
    process.env.API_BASE_URL || process.env.NEXT_PUBLIC_API_BASE_URL || '';
  try {
    const res = await fetch(
      `${apiBase}/jobs/status/${params.taskId}`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        cache: 'no-store',
      },
    );
    const data = await res.json();
    return new NextResponse(JSON.stringify(data), {
      status: res.status,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new NextResponse(
      JSON.stringify({ error: 'Failed to fetch job status' }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      },
    );
  }
}
