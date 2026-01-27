'use client';

import { useState } from 'react';
import { runPipeline, getJobStatus } from '../lib/api';
import { useToast } from './ToastProvider';
import Link from 'next/link';

interface Props {
  id: string;
}

export default function RunPipelineInline({ id }: Props) {
  const [status, setStatus] = useState<'idle' | 'running' | 'completed'>('idle');
  const [webViewLink, setWebViewLink] = useState<string | null>(null);
  const { showToast } = useToast();

  const handleClick = async () => {
    setStatus('running');
    try {
      const data = await runPipeline(id);
      const taskId =
        data.taskId ||
        data.task_id ||
        data.id ||
        data.jobId ||
        data.job_id;
      if (!taskId) {
        showToast('Failed to get task ID', 'error');
        setStatus('idle');
        return;
      }
      pollStatus(taskId);
    } catch (err) {
      showToast('Failed to start pipeline', 'error');
      setStatus('idle');
    }
  };

  const pollStatus = (taskId: string) => {
    const interval = 3000;
    const check = async () => {
      try {
        const result = await getJobStatus(taskId);
        const state =
          result.state || result.status || result.state?.status;
        if (state === 'SUCCESS' || state === 'COMPLETED') {
          setStatus('completed');
          showToast('Pipeline completed successfully', 'success');
          const link =
            result.webViewLink ||
            result.result?.webViewLink ||
            result.result?.web_view_link;
          if (link) {
            setWebViewLink(link);
          }
        } else if (state === 'FAILURE' || state === 'FAILED') {
          setStatus('idle');
          showToast('Pipeline failed', 'error');
        } else {
          setTimeout(check, interval);
        }
      } catch (error) {
        showToast('Failed to fetch job status', 'error');
        setStatus('idle');
      }
    };
    check();
  };

  return (
    <div className="flex items-center space-x-2">
      <button
        onClick={handleClick}
        disabled={status === 'running' || status === 'completed'}
        className={`px-4 py-1 rounded ${
          status === 'running' || status === 'completed'
            ? 'bg-gray-300'
            : 'bg-blue-600 text-white hover:bg-blue-700'
        }`}
      >
        {status === 'running'
          ? 'Running…'
          : status === 'completed'
          ? 'Completed'
          : 'Run Pipeline'}
      </button>
      {webViewLink && (
        <Link href={webViewLink} target="_blank">
          View Compliance XLSX
        </Link>
      )}
    </div>
  );
}
